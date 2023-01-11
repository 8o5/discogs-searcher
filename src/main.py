import discogs_client

d = discogs_client.Client('ExampleApplication/0.1')

release = d.release(1293022)
print(release.title)