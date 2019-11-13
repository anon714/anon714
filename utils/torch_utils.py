import torch


def load_checkpoint(model_path):
    weights = torch.load(model_path)
    epoch = None
    if 'epoch' in weights:
        epoch = weights.pop('epoch')
    if 'state_dict' in weights:
        state_dict = (weights['state_dict'])
    else:
        state_dict = weights
    return epoch, state_dict


def restore_model(model, pretrained_file):
    epoch, weights = load_checkpoint(pretrained_file)

    model_keys = set(model.state_dict().keys())
    weight_keys = set(weights.keys())

    # load weights by name
    weights_not_in_model = sorted(list(weight_keys - model_keys))
    model_not_in_weights = sorted(list(model_keys - weight_keys))
    if len(model_not_in_weights):
        print('Warning: There are weights in model but not in pre-trained.')
        for key in (model_not_in_weights):
            print(key)
            weights[key] = model.state_dict()[key]
    if len(weights_not_in_model):
        print('Warning: There are pre-trained weights not in model.')
        for key in (weights_not_in_model):
            print(key)
        from collections import OrderedDict
        new_weights = OrderedDict()
        for key in model_keys:
            new_weights[key] = weights[key]
        weights = new_weights

    model.load_state_dict(weights)
    return model