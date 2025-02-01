# Synthetic Data Generation Tool for Blender

Project developed in **2023** as part of my **Undergraduate Final Year Project** in **Mechatronics Engineering**, approved as a requirement for the **Bachelor's degree**. The project's theme is **"Development of a Computational Tool for Generating and Organizing Augmented Synthetic Data of Machine Elements"**. The tool is integrated into Blender®, an open-source 3D creation software, and allows the generation of augmented synthetic data for training deep learning models.

## Features

- **Language Selection**: Interface available in English and Portuguese.
- **Collection Creation**: Organize 3D models into collections for efficient management.
- **Model Import**: Import 3D models of machine elements from STL, PLY, or WRL files.
- **Material Application**: Apply predefined materials to simulate different physical properties.
- **Scene Setup**: Add lights and configure the scene for rendering.
- **Collection Rendering**: Render collections of objects with different camera angles.

## How to Use

### 1. Installation
- Copy the `scripts/` folder to Blender's add-ons directory.
- In Blender, go to `Edit > Preferences > Add-ons` and enable the add-on.

### 2. Using the Tool

#### Panel "Select Language"
- In the "Select Language" panel, choose between **English** and **Portuguese** to change the interface language.

#### Panel "Create Collection"
1. In the **"Enter collection name"** field, type a name for the new collection.
2. In the **"Enter render output path"** field, type the path where rendered images will be saved.
3. Click **"Add Collection Name"** and **"Add Render Output Path"** to confirm.
4. Click **"Create Collection"** to create the collection in the scene.

#### Panel "Import Models"
1. In the **"Enter import path"** field, type the path to the folder where the 3D models are stored.
2. In the dropdown **"File format"**, select the model format (STL, PLY, or WRL).
3. Click **"Import Models"** to import the models into the created collection.

#### Panel "Model Appearance"
1. In the dropdown **"Select View"**, choose the desired view (Isometric, Front, Top, etc.).
2. In the dropdown **"Select Material"**, choose the material to be applied (Stainless Steel, Brass, Bronze, etc.).
3. In the dropdown **"Select Collection"**, choose the collection of objects to receive the changes.
4. Click **"Apply Changes"** to apply the selected view and material.

#### Panel "Set Up Scene"
- Click **"Set Up Scene"** to add a light to the scene and prepare the environment for rendering.

#### Panel "Render Collections"
1. In the **"Set Frames Angle"** field, enter the desired angle between each frame of the rendering.
2. Click **"Set Frames"** to calculate the frame angles.
3. Click **"Render Collections"** to render the collections of objects with the defined camera angles.

## Project Structure
```
blender-data-generation-tool/
├── README.md
├── LICENSE
├── scripts/
│   ├── __init__.py
│   ├── main.py
│   ├── panels/
│   │   ├── language_panel.py
│   │   ├── collection_panel.py
│   │   ├── import_panel.py
│   │   ├── material_panel.py
│   │   ├── scene_panel.py
│   │   ├── render_panel.py
├── docs/
│   ├── images
│   ├── flowcharts
├── examples/
│   ├── sample_data
│   ├── output
```
## Requirements

- Blender 2.8 or higher.
- Python 3.7 or higher.

## License

This project is licensed under the MIT License. See the [LICENSE file](LICENSE) for details.
