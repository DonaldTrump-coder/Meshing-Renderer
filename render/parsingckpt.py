import torch
from internal.utils.gaussian_model_loader import GaussianModelLoader

class CKPT_Parser:
    def __init__(self, filename):
        device = torch.device("cuda")
        ckpt = torch.load(filename, map_location="cpu", weights_only=False)
        self.model = GaussianModelLoader.initialize_model_from_checkpoint(
                                ckpt,
                                device=device)
        self.model.freeze()
        self.model.pre_activate_all_properties()

    def get_model(self):
        return self.model
    #get the model for rendering
    
    def get_points(self):
        # get xyz of 2DGS in the model
        pass

    def get_params(self):
        # get all the parameters of the 2DGS model in a Tensor
        pass