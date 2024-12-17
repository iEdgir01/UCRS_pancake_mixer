# UCRS_pancake_mixer
This project provides functionality to generate a valid pancake stack based on specific rules.

## Installation Instructions

1. **Clone the repository:**
   
   ``git clone https://github.com/iEdgir01/UCRS_pancake_mixer.git``
   
   ``cd path/to/your/cloned/directory``
   
3. **Ensure you have Python installed: This script is written in Python.**
   
    You can download it from python.org.

## Usage

1. **Run the script**
    ```bash
    python pancake_mixer.py
    ```
2. **The script will prompt you to enter the pancake stack size and required pancakes.**
   
    **Format Guide:**
   
    Input Format: Enter the stack size followed by the required pancakes.
   
    Example: 4OG (4 is the size, O and G are the required pancakes).

## Pancake Identification

![{3720A3D7-AFAA-4C56-BE1A-894219D21C8E}](https://github.com/user-attachments/assets/a0f1a481-ca86-47df-80c6-f65109ab960f)

   
## Pancake stack Rules

  - Orange (O): Cannot be on the edge and must connect to two other pancakes.
  - Yellow (Y): Must be adjacent to another Yellow pancake.
  - White (W): Must have identical pancakes on both sides.
  - Grey (G): Must have different adjacent pancakes.

## Example
You want to create a pancake stack that contains 4 pancakes, and has to contain an Orange and a Grey Pancake.
```
Enter the pancake stack size and required pancakes (e.g., 4OG): 4OG
Generated stack: WOOG
Attempt number: 2
```

## Notes
to exit the script at any time, press ``CTRL+C``

## License
This project is licensed under the MIT License. See the LICENSE file for details.
