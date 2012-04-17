"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import reverse

from portal import models

class PortalRepositoryTest(TestCase):
    fixtures = ["resource.json", "repository.json", "collection.json"]
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_repo_list(self):
        """Test list of repositories."""
        response = self.client.get(reverse("repo_list"))
        self.assertEqual(response.status_code, 200)

    def test_repo_collections(self):
        """Test repository's list of collections."""
        response = self.client.get(reverse("repo_collections", kwargs={
            "slug": "wiener-library",
        }))
        self.assertEqual(response.status_code, 200)

    def test_repo_detail(self):
        """Test repo detail view."""
        response = self.client.get(reverse("repo_detail", kwargs={
            "slug": "wiener-library",
        }))
        self.assertEqual(response.status_code, 200)
        
    def test_repo_edit(self):
        """Test repo edit view."""
        response = self.client.get(reverse("repo_edit", kwargs={
            "slug": "wiener-library",
        }))
        self.assertEqual(response.status_code, 200)


class PortalCollectionTest(TestCase):
    fixtures = ["resource.json", "repository.json", "collection.json"]
    def setUp(self):
        self.slug = "caro-jella-letter-from-theresienstadt"
        self.testdata = {

        }
        for field in ["date_set", "othername_set",
                "script", "script_of_description",
                "language", "language_of_description"]:
            self.testdata["%s-INITIAL_FORMS" % field] = 0 
            self.testdata["%s-MAX_NUM_FORMS" % field] = 1
            self.testdata["%s-TOTAL_FORMS" % field] = 1

    def tearDown(self):
        pass

    def test_collection_list(self):
        """Test list of collections."""
        response = self.client.get(reverse("collection_list"))
        self.assertEqual(response.status_code, 200)

    def test_collection_detail(self):
        """Test collection detail view."""
        response = self.client.get(reverse("collection_detail", kwargs={
            "slug": self.slug,
        }))
        self.assertEqual(response.status_code, 200)

    def test_collection_create_get(self):
        """Test collection create view."""
        response = self.client.get(reverse("collection_create"))
        self.assertEqual(response.status_code, 200)

    def test_collection_create_post(self):
        """Test creating a collection."""
        repo = models.Repository.objects.all()[0]
        testname = "Test Create"
        self.assertEqual(models.Collection.objects.filter(
                name=testname).count(), 0)
        self.testdata.update({
            "identifier": "GB Test 0001",
            "name": testname,
            "repository": repo.pk,
            "language-0-value": "en",
        })
        response = self.client.post(reverse("collection_create"), self.testdata)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Collection.objects.filter(
                name=testname).count(), 1)
        c = models.Collection.objects.filter(name=testname)[0]
        self.assertIn("en", c.languages)
        self.assertEqual(testname, c.name)
        
    def test_collection_edit_get(self):
        """Test collection edit view."""
        response = self.client.get(reverse("collection_edit", kwargs={
            "slug": self.slug,
        }))
        self.assertEqual(response.status_code, 200)

    def test_collection_edit_post(self):
        """Test updating a collection."""
        c = models.Collection.objects.get(slug=self.slug)
        self.testdata.update({
            "identifier": "Test",
            "name": "Test",
            "repository": c.repository.pk
        })
        response = self.client.post(reverse("collection_edit", kwargs={
            "slug": self.slug,
        }), self.testdata)
        self.assertEqual(response.status_code, 302)
        c = models.Collection.objects.get(slug=self.slug)
        self.assertEqual(c.name, "Test")
        
    def test_collection_edit_add_langprop(self):
        """Test updating a collection."""
        c = models.Collection.objects.get(slug=self.slug)
        self.assertNotIn("de", c.languages)
        self.testdata.update({
            "identifier": "Test",
            "name": "Test",
            "repository": c.repository.pk,
            "language-0-value": "de",
        })
        response = self.client.post(reverse("collection_edit", kwargs={
            "slug": self.slug,
        }), self.testdata)
        self.assertEqual(response.status_code, 302)
        c = models.Collection.objects.get(slug=self.slug)
        self.assertIn("de", c.languages)
        
    def test_collection_edit_add_alt_name(self):
        """Test updating a collection."""
        c = models.Collection.objects.get(slug=self.slug)
        self.assertNotIn("Alt Test", c.other_names)
        self.testdata.update({
            "identifier": "Test",
            "name": "Test",
            "repository": c.repository.pk,
            "othername_set-0-name": "Alt Test",
        })
        response = self.client.post(reverse("collection_edit", kwargs={
            "slug": self.slug,
        }), self.testdata)
        self.assertEqual(response.status_code, 302)
        c = models.Collection.objects.get(slug=self.slug)
        self.assertIn("Alt Test", c.other_names)
        
    def test_collection_edit_with_error(self):
        """Test updating a collection."""
        c = models.Collection.objects.get(slug=self.slug)
        self.assertNotIn("Alt Test", c.other_names)
        self.testdata.update({
            "identifier": "",
            "name": "Test",
            "repository": c.repository.pk,
            "othername_set-0-name": "Alt Test",
        })
        response = self.client.post(reverse("collection_edit", kwargs={
            "slug": self.slug,
        }), self.testdata)
        self.assertEqual(response.status_code, 200)
        c = models.Collection.objects.get(slug=self.slug)
        self.assertNotIn("Alt Test", c.other_names)
        
