from django.shortcuts import render
from . models import load_model
from cnn_app.input_data_preprocessing import apply_test_transforms
from PIL import Image
model = None

# Create your views here.
is_model_loaded = False
if is_model_loaded == False:
    model = load_model()
    is_model_loaded = True



def predict_image(image):
    image_tensor = apply_test_transforms(image)
    # image_tensor = image_tensor.unsqueeze_(0)
    input = image_tensor.cuda()
    output = model(input[None, ...])
    index = output.data.cpu().numpy().argmax()
    return index



def homeview(request):
    if request.method == "GET":
        return render(request, 'index.html')
    if request.method == "POST" and request.FILES['myfile']:
        input_image = request.FILES['myfile']
        print(input_image)
        print('uploading image')
        result = predict_image(Image.open(input_image))
        if result == 0:
            result = "given image is cat"
        if result == 1:
            result = "given image is dog"
        return render(request, 'index.html', {"result":result})


print(model)
print(model.state_dict())


