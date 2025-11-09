# 🎨 Hunyuan_OS - 3D Model Gallery

<div align="center">

![Hunyuan3D](https://img.shields.io/badge/Powered%20by-Hunyuan3D%202.0-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Models](https://img.shields.io/badge/3D%20Models-Growing-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**A curated collection of 3D models generated using Tencent's Hunyuan3D-2.0**

[🎯 Features](#-features) • [🚀 Quick Start](#-quick-start) • [📦 Model Gallery](#-model-gallery) • [🤝 Contributing](#-contributing) • [📚 Resources](#-resources)

---

</div>

## 📖 About This Project

Welcome to **Hunyuan_OS** - a showcase repository featuring high-quality 3D models generated using Tencent's cutting-edge **Hunyuan3D-2.0** model. This repository serves as both a gallery and a resource for anyone interested in AI-generated 3D content.

### What is Hunyuan3D-2.0?

Hunyuan3D-2.0 is a state-of-the-art large-scale 3D synthesis system developed by Tencent that can generate high-resolution textured 3D assets from images or text prompts. It features:

- 🎯 **Image-to-3D**: Transform 2D images into detailed 3D models
- ✍️ **Text-to-3D**: Generate 3D objects from text descriptions
- 🎨 **High-Quality Textures**: Vibrant, detailed texture maps
- ⚡ **Advanced Pipeline**: Two-stage generation (shape + texture)

### 🔗 Official Resources

- **Hugging Face**: [https://huggingface.co/tencent/Hunyuan3D-2](https://huggingface.co/tencent/Hunyuan3D-2)
- **GitHub**: [https://github.com/Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)
- **Official Site**: [https://3d.hunyuan.tencent.com/](https://3d.hunyuan.tencent.com/)
- **Paper (arXiv)**: [2501.12202](https://arxiv.org/abs/2501.12202)

---

## ✨ Features

- 📂 **Organized Model Collection**: Each model includes shape, texture, reference image, and preview
- 🖼️ **Visual Documentation**: Screenshots and original images for each 3D model
- 🎮 **Easy Viewing**: Built-in GLB file viewer for quick model inspection
- ☁️ **Kaggle/Colab Ready**: Complete Jupyter notebook for generating your own models (FREE GPU!)
- 🔄 **Regular Updates**: New models added frequently
- 🤝 **Community Driven**: Open for contributions from the community

---

## 🚀 Quick Start

### 🎯 Generate Your Own 3D Models (Recommended)

**Want to create 3D models yourself?** We've made it easy!

#### ☁️ **Use Kaggle or Google Colab (Recommended - FREE GPU!)**

The easiest way to generate models is using our ready-to-use Jupyter notebook on Kaggle or Google Colab:

1. **Download the notebook**: [Hunyuan3D_Kaggle_Guide.ipynb](./Hunyuan3D_Kaggle_Guide.ipynb)
2. **Upload to Kaggle or Google Colab**
3. **Enable GPU** (T4 recommended)
4. **Run all cells** and wait for your Gradio URL
5. **Generate models** from images or text prompts!

📝 **Why Kaggle/Colab?**
- ✅ **Free GPU access** (much faster than CPU)
- ✅ **Pre-configured environment** (no local setup needed)
- ✅ **Step-by-step guide** with all commands
- ✅ **Works out of the box** (tested and optimized)
- ✅ **~5-12 minutes per model** on T4 GPU

The notebook includes:
- Complete installation instructions
- Dependency management
- Gradio web interface setup
- Tips for best results
- Troubleshooting guide

---

### 💻 Local Viewing

If you just want to view existing models from this gallery:

#### Prerequisites

```bash
# Python 3.8 or higher required
python --version
```

#### Installation

1. **Clone the repository**

```bash
git clone https://github.com/ManvithGopu13/Hunyuan_OS.git
cd Hunyuan_OS
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

#### 🎮 Viewing 3D Models

We provide a convenient GLB viewer to inspect all 3D models in this repository.

```bash
python display_glb.py
```

This will launch an interactive viewer where you can:
- ✅ Browse all available 3D models
- ✅ View textured and untextured versions
- ✅ Rotate, zoom, and inspect models
- ✅ Compare with reference images

---

## 📦 Model Gallery

### Current Collection

Our repository currently contains the following 3D models:

#### 🏠 Room Models

<table>
  <tr>
    <td align="center">
      <b>Room 1 (Google)</b><br>
      <img src="3d_models/room_google_1/room.jpeg" width="200" alt="Room 1"/><br>
      <i>Modern interior space</i><br>
      <a href="3d_models/room_google_1/">View Model</a>
    </td>
    <td align="center">
      <b>Room 2</b><br>
      <img src="3d_models/room_2/room_2.jpeg" width="200" alt="Room 2"/><br>
      <i>Detailed room layout</i><br>
      <a href="3d_models/room_2/">View Model</a>
    </td>
  </tr>
</table>

### 📁 Model Structure

Each model folder contains:

```
model_name/
├── [name]_shape.glb    # Untextured 3D geometry
├── [name]_tex.glb      # Textured 3D model
├── [name].jpeg         # Original input image
└── [name]_3d.png       # 3D model screenshot
```

---

## 🛠️ Usage Guide

### Option 1: View Models with Our Script

```bash
# View all models interactively
python display_glb.py
```

### Option 2: Open Models in 3D Software

The GLB files can be opened in various 3D applications:

- **Blender**: Free and open-source (Recommended)
- **Autodesk Maya**: Professional 3D software
- **3ds Max**: Industry-standard modeling tool
- **Online Viewers**: [gltf-viewer.donmccurdy.com](https://gltf-viewer.donmccurdy.com/)

### Option 3: Use in Web Applications

```html
<!-- Example: Using model-viewer for web -->
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<model-viewer src="path/to/model_tex.glb" auto-rotate camera-controls></model-viewer>
```

---

## 💻 Local Setup (Advanced Users)

Want to run Hunyuan3D-2.0 locally? Here's a complete guide!

### 📋 System Requirements

**Minimum:**
- **GPU**: NVIDIA with 12GB+ VRAM (RTX 3060 12GB, RTX 4070+)
- **Python**: 3.9 - 3.11 (3.10 recommended)
- **CUDA**: 11.8 or 12.1
- **RAM**: 16GB+ system memory
- **Storage**: 50GB+ free space

**Recommended:**
- **GPU**: RTX 4080/4090 or A5000/A6000 (16GB+ VRAM)
- **RAM**: 32GB+
- **Storage**: SSD with 100GB+ free

### 🔧 Installation Steps

1. **Install Prerequisites**
   ```bash
   # Python 3.10
   # CUDA 11.8 or 12.1
   # Visual Studio Build Tools (Windows) or build-essential (Linux)
   ```

2. **Clone Official Repository**
   ```bash
   git clone https://github.com/Tencent-Hunyuan/Hunyuan3D-2.git
   cd Hunyuan3D-2
   ```

3. **Create Virtual Environment**
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # Linux/macOS
   # OR
   venv\Scripts\activate  # Windows
   ```

4. **Install PyTorch with CUDA**
   ```bash
   # CUDA 11.8
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   
   # CUDA 12.1
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   ```

5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install transformers==4.46.1 diffusers==0.30.2 optimum==1.23.2 accelerate==0.33.0
   ```

6. **Build Custom Modules**
   ```bash
   # Custom rasterizer
   cd hy3dgen/texgen/custom_rasterizer && python setup.py install && cd ../../..
   
   # Differentiable renderer
   cd hy3dgen/texgen/differentiable_renderer && python setup.py install && cd ../../..
   ```

7. **Launch Gradio App**
   ```bash
   python gradio_app.py --enable_t23d --profile 5
   ```

📘 **Detailed Guide**: See [Hunyuan3D_Kaggle_Guide.ipynb](./Hunyuan3D_Kaggle_Guide.ipynb) for complete local setup instructions.

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### ⚠️ Installation Problems

**CUDA Out of Memory**
- Reduce profile: Use `--profile 3` instead of `--profile 5`
- Close other GPU applications
- Reduce input image resolution to 512x512
- Restart Python kernel

**Module Not Found Errors**
```bash
# Reinstall specific versions
pip uninstall -y transformers diffusers
pip install --no-cache-dir transformers==4.46.1 diffusers==0.30.2
```

**Build Errors (Windows)**
- Install Visual Studio Build Tools with "Desktop development with C++"
- Restart terminal after installation

**Build Errors (Linux)**
```bash
sudo apt-get install build-essential python3-dev
pip install wheel setuptools
```

#### 🔧 Runtime Issues

**Slow Generation (>30 min)**
- Check GPU is enabled: `torch.cuda.is_available()` should return `True`
- Verify GPU usage: `nvidia-smi`
- Ensure CUDA drivers are up to date

**Gradio Interface Not Loading**
- Check firewall settings
- Try different port: `python gradio_app.py --port 7861`
- Look for public URL in terminal output

**Low Quality Models**
- Use higher profile (--profile 5)
- Provide clear, well-lit input images
- Use simple backgrounds
- Try front-facing object views
- Input resolution: 512x512 to 1024x1024

#### 💾 File Issues

**Can't Find Generated Models**

Check these directories:
- `./outputs/`
- `./gradio_cache/`
- `./tmp/`

Use the file finder in our notebook (Step 10) or run:
```python
find . -name "*.glb" -type f
```

#### ⚙️ Performance Optimization

**Speed Up Generation:**
1. Enable GPU in system settings
2. Use CUDA 11.8 or 12.1 (not CPU-only PyTorch)
3. Close unnecessary applications
4. Use lower profile for testing: `--profile 3`
5. Clear GPU cache:
   ```python
   import torch
   torch.cuda.empty_cache()
   ```

**Memory Optimization:**
- Generate one model at a time
- Restart kernel between generations
- Monitor GPU memory: `nvidia-smi`

#### 🆘 Quick Diagnostics

Run these commands to check your setup:

```bash
# Check Python version
python --version  # Should be 3.9-3.11

# Check CUDA
nvcc --version
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}')"

# Check GPU
nvidia-smi

# Test PyTorch
python -c "import torch; print(f'PyTorch: {torch.__version__}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"None\"}')"
```

### 📚 Need More Help?

- **📓 Complete Guide**: Check our [Jupyter Notebook](./Hunyuan3D_Kaggle_Guide.ipynb) for detailed troubleshooting
- **🐛 Report Issues**: [GitHub Issues](https://github.com/ManvithGopu13/Hunyuan_OS/issues)
- **💬 Discussions**: [Community Forum](https://github.com/ManvithGopu13/Hunyuan_OS/discussions)
- **📖 Official Docs**: [Hunyuan3D-2 Repository](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)

---

## 🤝 Contributing

We welcome contributions from the community! Whether you've generated amazing 3D models or want to improve the repository, your help is appreciated.

### How to Contribute:

1. 📖 **Read the Contributing Guide**: [CONTRIBUTING.md](CONTRIBUTING.md)
2. 🍴 **Fork the Repository**
3. 🎨 **Generate Your Models** using Hunyuan3D-2.0
4. 📤 **Submit a Pull Request** with your models

### What You Can Contribute:

- ✅ 3D models generated from images
- ✅ 3D models generated from text prompts
- ✅ Improvements to the display script
- ✅ Documentation enhancements
- ✅ Bug fixes and optimizations

Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🔄 Update Schedule

This repository is **actively maintained** and regularly updated with new models. 

- 📅 **Latest Update**: November 9, 2025
- 🆕 **Total Models**: 2 (and growing!)
- ⭐ **Update Frequency**: Regular additions

**Watch this repository** to get notified when new models are added!

---

## 📚 Resources

### Learn About Hunyuan3D-2.0

- 📄 [Technical Paper](https://arxiv.org/abs/2501.12202) - Deep dive into the architecture
- 🎓 [Hugging Face Model Card](https://huggingface.co/tencent/Hunyuan3D-2) - Model details and API
- 💻 [GitHub Repository](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) - Source code and examples
- 🌐 [Official Website](https://3d.hunyuan.tencent.com/) - Try it online

### Getting Started with 3D Generation

```python
# Example: Generate a 3D model from an image
from hy3dgen.shapegen import Hunyuan3DDiTFlowMatchingPipeline
from hy3dgen.texgen import Hunyuan3DPaintPipeline

# Generate shape
shape_pipeline = Hunyuan3DDiTFlowMatchingPipeline.from_pretrained('tencent/Hunyuan3D-2')
mesh = shape_pipeline(image='your_image.png')[0]

# Add texture
texture_pipeline = Hunyuan3DPaintPipeline.from_pretrained('tencent/Hunyuan3D-2')
textured_mesh = texture_pipeline(mesh, image='your_image.png')

# Save the model
textured_mesh.export('output.glb')
```

### Community Resources

- 🎨 [ComfyUI Integration](https://github.com/MrForExample/ComfyUI-3D-Pack)
- 🪟 [Windows Bundle](https://huggingface.co/YanWenKun/Hunyuan3D-2-for-windows)
- 🎮 [Blender Addon](https://github.com/Tencent-Hunyuan/Hunyuan3D-2#blender-addon)

---

## 📊 Model Statistics

| Metric | Value |
|--------|-------|
| Total Models | 2 |
| Model Types | Rooms, Interiors |
| Formats | GLB (shape + texture) |
| Average Quality | High Resolution |
| Repository Status | 🟢 Active |

---

## 🎯 Use Cases

This model collection can be used for:

- 🎮 **Game Development**: Asset creation for games
- 🏗️ **Architecture**: Visualization and planning
- 🎬 **Film & Animation**: 3D content for media projects
- 🎓 **Education**: Learning 3D modeling and AI
- 🔬 **Research**: Studying AI-generated 3D content
- 🎨 **Art & Design**: Creative projects and prototyping

---

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Note**: Models are generated using Hunyuan3D-2.0, which is subject to the [Tencent Hunyuan Community License](https://huggingface.co/tencent/Hunyuan3D-2/blob/main/LICENSE.txt).

---

## 🙏 Acknowledgments

- **Tencent Hunyuan3D Team** - For developing the amazing Hunyuan3D-2.0 model
- **Open Source Community** - For tools and libraries that make this possible
- **Contributors** - Everyone who has submitted models to this repository

### Special Thanks

This project builds upon the groundbreaking work of:
- [DINOv2](https://github.com/facebookresearch/dinov2)
- [Stable Diffusion](https://github.com/Stability-AI/stablediffusion)
- [FLUX](https://github.com/black-forest-labs/flux)
- [Hugging Face Diffusers](https://github.com/huggingface/diffusers)

---

## 📞 Contact & Support

- 🐛 **Issues**: [Report bugs or request features](https://github.com/ManvithGopu13/Hunyuan_OS/issues)
- 💡 **Discussions**: [Ask questions or share ideas](https://github.com/ManvithGopu13/Hunyuan_OS/discussions)
- 📧 **Email**: manvithgopu1394@gmail.com

---

## 🌟 Star History

If you find this repository useful, please consider giving it a star! ⭐

It helps others discover this resource and motivates continued development.

---

<div align="center">

**Made with ❤️ using [Hunyuan3D-2.0](https://huggingface.co/tencent/Hunyuan3D-2)**

*"Living out everyone's imagination on creating and manipulating 3D assets."*

[⬆ Back to Top](#-hunyuan_os---3d-model-gallery)

</div>

