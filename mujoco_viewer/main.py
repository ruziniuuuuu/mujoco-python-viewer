import argparse
import mujoco
import mujoco_viewer.mujoco_viewer as mujoco_viewer
import sys

def main():
    # Create command line argument parser
    parser = argparse.ArgumentParser(description='MuJoCo Model Viewer')
    parser.add_argument('xml_path', type=str, help='Path to MuJoCo XML model file')
    
    try:
        args = parser.parse_args()
        
        # Load model
        model = mujoco.MjModel.from_xml_path(args.xml_path)
        data = mujoco.MjData(model)

        # Create viewer object
        viewer = mujoco_viewer.MujocoViewer(model, data)

        # Continuously render until window is closed
        while viewer.is_alive:
            mujoco.mj_step(model, data)
            viewer.render()

    except FileNotFoundError:
        print(f"Error: XML file not found '{args.xml_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)
    finally:
        # Ensure viewer is properly closed
        if 'viewer' in locals():
            viewer.close()

if __name__ == "__main__":
    main() 