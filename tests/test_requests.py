def test_create_blog_post(client):
    response = client.post("/admin/posts", data={
        "title": "A test blog post",
        "slug": "a-test-blog-post",
        "content": "# Test\n\nThis is my test blog post! Isn't it *fantastic*?",
        "tags": ["foo", "bar"],
        "draft": True
    })
    response = client.get("/posts/a-test-blog-post.html")
    assert response.status_code == 200
