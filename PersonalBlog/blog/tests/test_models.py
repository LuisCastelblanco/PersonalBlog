from django.test import TestCase
from blog.models import post, image, comment
from django.urls import reverse

class PostModelTest(TestCase):

    def setUp(self):
        post.objects.create(title="Test Post", entry="Test Content")

    def test_post_content(self):
        p = post.objects.get(title="Test Post")
        self.assertEqual(p.entry, "Test Content")  

    def test_post_str(self):
        p = post.objects.get(title="Test Post")
        self.assertEqual(str(p), "Test Post")

    def test_post_dateOfEntry(self):
        p = post.objects.get(title="Test Post")
        self.assertIsNotNone(p.dateOfEntry)  # Assuming dateOfEntry is not "Test Content"

    def test_post_dateOfUpdate(self):
        p = post.objects.get(title="Test Post")
        self.assertIsNotNone(p.dateOfUpdate)  # Assuming dateOfUpdate is not "Test Content"

class ImageModelTest(TestCase):

    def setUp(self):
        p = post.objects.create(title="Test Post", entry="Test Content")
        image.objects.create(post=p, image="images/test.jpg")

    def test_image_content(self):
        i = image.objects.get(image="images/test.jpg")
        self.assertEqual(i.post.title, "Test Post")
    
    def test_image_str(self):
        i = image.objects.get(image="images/test.jpg")
        self.assertEqual(str(i), "/images/test.jpg")

    def test_image_dateOfEntry(self):
        i = image.objects.get(image="images/test.jpg")
        self.assertIsNotNone(i.dateOfEntry)  # Assuming dateOfEntry is not "Test Content"

class CommentModelTest(TestCase):
    
    def setUp(self):
        p = post.objects.create(title="Test Post", entry="Test Content")
        comment.objects.create(post=p, name="Test Name", content="Test Comment")

    def test_comment_content(self):
        c = comment.objects.get(name="Test Name")
        self.assertEqual(c.content, "Test Comment")
        
    def test_comment_str(self):
        c = comment.objects.get(name="Test Name")
        self.assertEqual(str(c), "Test Name")
        
    def test_comment_dateOfComment(self):
        c = comment.objects.get(name="Test Name")
        self.assertIsNotNone(c.dateOfComment)  # Assuming dateOfComment is not "Test Content"

