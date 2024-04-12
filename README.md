# ✨Sparkjoy✨

*A blog engine that sparks joy*

# Goals

Static Site Generators (SSGs) are great, especially for blogs where the content
doesn't change very often. However, I've come to realize that I've never really
liked the "commit to publish" model for blogs. For lack of a better term, it
didn't "spark joy".

I want writing to feel responsive, and I want to be able to write from
anywhere, like you can with a traditional blog engine. At the same time, I
really like the file-oriented nature and high performance of SSGs. This project
is an attempt to combine the best features of both.

# Features

 - Built-in post editor.
 - File uploads.
 - Mobile-friendly UI.
 - Posts are plain Markdown, following the [File over app][file-over-app]
   philosophy.

# Run

```sh
FLASK_DEBUG=1 flask run
```

[file-over-app]: https://stephango.com/file-over-app
