from django.test import TestCase
from django.db import IntegrityError

from .models import *


class BlogModelTests(TestCase):

    def test_domain_is_unique(self):
        """
        tests blogs cannot have same domain
        """
        try:
            blog1 = Blog(title="testBlog1", description="testDesc1", domain="http://test.com", is_public=True)
            blog1.save()
            blog2 = Blog(title="testBlog2", description="testDesc2", domain="http://test.com", is_public=False)
            blog2.save()
            self.fail("should not allow creating another blog with same domain")
        except IntegrityError:
            pass
	
    def test_cover_image_defaults_to_blank(self):
        """
        tests cover image defaults to blank
        """
        blog = Blog(title="testBlog", description="test", domain="http://test.com")
        self.assertEqual(blog.cover_image, None)
	
	
class PostModelTests(TestCase):

    def test_post_can_contain_multiple_tags(self):
        """
        tests that a post can contain multiple tags
        """
        category1 = Category(name='category1')
        category1.save()
        tag1 = Tag(name='tag1')
        tag1.save()
        tag2 = Tag(name='tag2')
        tag2.save()
        user = User(1)
        user.save()
        blog = Blog(title='testBlog', description='test', domain='http://test.com', owner=user)
        blog.save()
        post = Post(title="testPost", body="testBody", category=category1, blog=blog)
        post.save()
        post.tag.add(tag1)
        post.tag.add(tag2)
        pass
	
	
class CategoryModelTests(TestCase):

    def test_name_is_unique(self):
        """
        tests categories cannot have same name
        """
        try:
            category1 = Category(name="testCategory")
            category1.save()
            category2 = Category(name="testCategory")
            category2.save()
            self.fail("should not allow creating another category with same name")
        except IntegrityError:
            pass
	
	
class TagModelTests(TestCase):

    def test_name_is_unique(self):
        """
        tests tags cannot have same name
        """
        try:
            tag1 = Tag(name="testTag")
            tag1.save()
            tag2 = Tag(name="testTag")
            tag2.save()
            self.fail("should not allow creating another tag with same name")
        except IntegrityError:
            pass
	