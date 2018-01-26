import glob
import io
import json
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient()
file_names = glob.glob('sample_images/*.jpg')
results_dic = {}

for file_name in file_names:
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    res_arr = []
    for label in labels:
        obj = {}
        obj['description'] = label.description
        obj['score'] = label.score
        obj['mid'] = label.mid
        res_arr.append(obj)

    results_dic[file_name] = res_arr

print(results_dic)

with open('test_labels.json', 'w') as f:
    json.dump(results_dic, f)
