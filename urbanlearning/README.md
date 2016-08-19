###UrbanLearning
####Deep Conventional Neural Network RESTFUL Api for Social Media Image Tagging 

Run:

```python
python app.py
```

For image classification[2]:

```python
http://server_ip:server_port/urbanlearning/api/v1.0/classify/<str:image_id>
```

For object detection[2]:

```python
http://server_ip:server_port/urbanlearning/api/v1.0/detect/<str:image_id>
```

For scene classification[3]:

```python
http://server_ip:server_port/urbanlearning/api/v1.0/scene/<str:image_id>
```

Example result:

```python
{
  "image": "994823142033453102_188893963", 
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
  "status": 200, 
  "task": "image classification"
}
```

####References
1. Deng, Jia, et al. "Imagenet: A large-scale hierarchical image database." Computer Vision and Pattern Recognition, 2009. CVPR 2009. IEEE Conference on. IEEE, 2009.
2. He, Kaiming, et al. "Deep residual learning for image recognition." arXiv preprint arXiv:1512.03385 (2015).
3. B. Zhou, A. Lapedriza, J. Xiao, A. Torralba, and A. Oliva Learning Deep Features for Scene Recognition using Places Database. Advances in Neural Information Processing Systems 27 (NIPS) spotlight, 2014.


