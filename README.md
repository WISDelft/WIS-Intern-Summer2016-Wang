###Urban Image Tagging with CNN

b.wang-6@student.tudelft.nl

The project contains three folders:

1. `urbanlearning`, the api folder, a restful api provide three state-of-the-art deep learning models.
2. `migration`, data migration scripts, migrate data from postgresql to mongodb.
3. `client`, client side of automatic image tagging, annotations were stored into mongodb database.

First start api

```python
./start_api.sh
```

Then start client:

```python
./start_client.sh
```
