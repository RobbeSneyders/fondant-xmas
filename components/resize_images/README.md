# Resize images

## Description
Component that resizes images based on given width and height

## Inputs / outputs

### Consumes
**This component consumes:**

- image: binary





### Produces
**This component produces:**

- image: binary



## Arguments

The component takes the following arguments to alter its behavior:

| argument | type | description | default |
| -------- | ---- | ----------- | ------- |
| resize_width | int | The width to resize to | / |
| resize_height | int | The height to resize to | / |

## Usage

You can add this component to your pipeline using the following code:

```python
from fondant.pipeline import Pipeline


pipeline = Pipeline(...)

dataset = pipeline.read(...)

dataset = dataset.apply(
    "resize_images",
    arguments={
        # Add arguments
        # "resize_width": 0,
        # "resize_height": 0,
    },
)
```

