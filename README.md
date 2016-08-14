###UrbanLearning
####Deep Conventional Neural Network RESTFUL Api for Social Media Image Tagging 

Run:

```python
python app.py
```

For image classification:

```python
http://server_ip:server_port/urbanlearning/api/v1.0/classify/<str:image_id>
```

For object detection:

```python
http://server_ip:server_port/urbanlearning/api/v1.0/detect/<str:image_id>
```

Example result:

```python
{
  "result": [
    {
      "label": "n04371430 swimming trunks, bathing trunks", 
      "prob": "0.000014"
    }, 
    {
      "label": "n09421951 sandbar, sand bar", 
      "prob": "0.000001"
    }, 
    {
      "label": "n09288635 geyser", 
      "prob": "0.000112"
    }, 
    {
      "label": "n02807133 bathing cap, swimming cap", 
      "prob": "0.000088"
    }, 
    {
      "label": "n09468604 valley, vale", 
      "prob": "0.000537"
    }
  ], 
  "status": 200
}
```

####References


