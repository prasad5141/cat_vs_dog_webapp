from torchvision import transforms


def apply_test_transforms(inp):
    # out = transforms.functional.resize(inp, [224])
    # out = transforms.functional.to_tensor(out)
    # out = transforms.functional.normalize(out, [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    transform = transforms.Compose([transforms.Resize(224),
                               transforms.CenterCrop(224),
                               transforms.ToTensor()])
    result = transform(inp)
    return result


    