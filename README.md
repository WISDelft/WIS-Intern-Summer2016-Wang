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
      "label": "n06794110 street sign", 
      "prob": 0.2572062313556671
    }, 
    {
      "label": "n02776631 bakery, bakeshop, bakehouse", 
      "prob": 0.1639353483915329
    }, 
    {
      "label": "n06596364 comic book", 
      "prob": 0.08545635640621185
    }, 
    {
      "label": "n04070727 refrigerator, icebox", 
      "prob": 0.048737164586782455
    }, 
    {
      "label": "n02977058 cash machine, cash dispenser, automated teller machine, automatic teller machine, automated teller, automatic teller, ATM", 
      "prob": 0.028399966657161713
    }
  ], 
  "status": 200
}
```

####References


