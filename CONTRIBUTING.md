# Contributing to Hunyuan_OS

Thank you for your interest in contributing to this 3D models repository! This guide will help you get started with contributing your own 3D models generated using Tencent's Hunyuan3D-2.0.

## 📋 Table of Contents

- [How to Contribute](#how-to-contribute)
- [Model Submission Guidelines](#model-submission-guidelines)
- [File Structure](#file-structure)
- [Quality Standards](#quality-standards)
- [Pull Request Process](#pull-request-process)

## 🤝 How to Contribute

We welcome contributions from everyone! Whether you're generating 3D models from images or text, your creations are valuable to the community.

### Ways to Contribute:

1. **Submit 3D Models**: Share your generated 3D models with the community
2. **Improve Documentation**: Help improve README, guides, or examples
3. **Report Issues**: Found a problem with a model or the display script? Let us know!
4. **Enhance Tools**: Improve the `display_glb.py` script or create new utilities

## 📦 Model Submission Guidelines

### Before Submitting:

1. **Generate your model** using [Hunyuan3D-2.0](https://huggingface.co/tencent/Hunyuan3D-2)
2. **Test your model** using the provided `display_glb.py` script
3. **Prepare all required files** (see File Structure below)

### Required Files for Each Model:

```
3d_models/
└── your_model_name/
    ├── model_shape.glb       # Shape-only 3D model
    ├── model_tex.glb         # Textured 3D model
    ├── reference_image.jpeg  # Original input image
    └── model_3d.png         # Screenshot of the 3D model
```

### File Naming Conventions:

- **Folder Name**: Use descriptive, lowercase names with underscores (e.g., `modern_chair`, `fantasy_castle`)
- **GLB Files**: 
  - `{name}_shape.glb` - Untextured geometry
  - `{name}_tex.glb` - Textured model
- **Images**:
  - `{name}.jpeg` - Original input image
  - `{name}_3d.png` - 3D model screenshot

## 📁 File Structure

Organize your submission following this structure:

```
3d_models/
└── [your_model_name]/
    ├── [name]_shape.glb      # Required: Geometry file
    ├── [name]_tex.glb        # Required: Textured model
    ├── [name].jpeg           # Required: Input reference image
    └── [name]_3d.png         # Required: 3D preview screenshot
```

### Example:

```
3d_models/
└── coffee_mug/
    ├── coffee_mug_shape.glb
    ├── coffee_mug_tex.glb
    ├── coffee_mug.jpeg
    └── coffee_mug_3d.png
```

## ✨ Quality Standards

To maintain high-quality contributions, please ensure:

### 3D Models:
- ✅ Models are generated using Hunyuan3D-2.0
- ✅ GLB files are not corrupted and can be opened
- ✅ File sizes are reasonable (preferably under 50MB per file)
- ✅ Both shape and textured versions are included

### Images:
- ✅ Reference images are clear and well-lit
- ✅ Screenshots show the model from a good viewing angle
- ✅ Image formats: JPEG for photos, PNG for screenshots
- ✅ Reasonable resolution (1024x1024 or higher recommended)

### Documentation:
- ✅ Include a brief description in your pull request
- ✅ Mention the input prompt (if text-to-3D) or describe the input image
- ✅ Note any special generation parameters used

## 🔄 Pull Request Process

### Step 1: Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/Hunyuan_OS.git
cd Hunyuan_OS
```

### Step 2: Create a Branch

```bash
git checkout -b add-model-[your-model-name]
```

### Step 3: Add Your Model

```bash
# Create your model folder
mkdir -p 3d_models/your_model_name

# Add your files
cp /path/to/your/files/* 3d_models/your_model_name/

# Stage your changes
git add 3d_models/your_model_name/
```

### Step 4: Commit Your Changes

```bash
git commit -m "Add 3D model: [brief description]

- Generated using Hunyuan3D-2.0
- Input: [describe your input image/prompt]
- Includes shape, texture, reference image, and screenshot"
```

### Step 5: Push and Create Pull Request

```bash
git push origin add-model-[your-model-name]
```

Then go to GitHub and create a Pull Request with:

**Title**: `Add 3D Model: [Model Name]`

**Description Template**:
```markdown
## Model Information

**Model Name**: [Your model name]
**Generation Method**: Image-to-3D / Text-to-3D
**Input Description**: [Describe your input]

## Files Included

- [ ] Shape GLB file
- [ ] Textured GLB file
- [ ] Reference image
- [ ] 3D screenshot

## Additional Notes

[Any special information about the model, generation parameters, or interesting observations]
```

### Step 6: Review Process

- A maintainer will review your submission
- Address any requested changes
- Once approved, your model will be merged!

## 🐛 Reporting Issues

Found a problem? Please open an issue with:

- **Clear description** of the problem
- **Steps to reproduce** (if applicable)
- **Expected vs actual behavior**
- **Screenshots or error messages** (if relevant)

## 💡 Suggestions and Discussions

Have ideas for improving the repository? Open a discussion or issue! We're always looking for ways to make this resource better.

## 📜 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Give credit where credit is due

## ❓ Questions?

If you have questions about contributing, feel free to:
- Open an issue with the `question` label
- Check existing issues and discussions
- Reach out to the repository maintainers

## 🙏 Thank You!

Your contributions help build a valuable resource for the 3D generation community. Thank you for sharing your work!

---

**Happy Contributing!** 🎨✨

Generated with ❤️ using [Hunyuan3D-2.0](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)

