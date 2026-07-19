import barcode
from barcode.writer import ImageWriter

# Function to take student info
def take_student_info():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    return student_id, name

# Function to generate Barcode
def generate_barcode(student_id, name):
    data = f"Student ID: {student_id}, Name: {name}"
    # Code128 barcode class
    Code128 = barcode.get_barcode_class('code128')
    my_barcode = Code128(data, writer=ImageWriter())
    filename = my_barcode.save("Barcode_1")  # Saves as Barcode_1.png
    print("✅ Barcode generated successfully:", filename)

# Main function
def main():
    student_id, name = take_student_info()
    generate_barcode(student_id, name)

if __name__ == "__main__":
    main()

