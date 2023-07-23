# federated-python-example

example how to build graphql microservice, that can be joined in apollo federation

``` bash
# how to run
docker image build -t <your-image-tag> .
docker run -p 5555:80 <your-image-tag>

# go to http://localhost:5555/graphql
```

## run example query

``` graphql

query getAllUsers {
  allUsers{
    id
    email
  }
}

```
