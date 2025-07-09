import fitz  # PyMuPDF
import pdb
def get_longest_words(page, top_n=5):
    words = page.get_text("words")  # (x0, y0, x1, y1, word, block_no, line_no, word_no)
    out = page.get_text("dict")
    #pdb.set_trace()
    no_rot =0
    left_rot =0
    right_rot =0
    print('len--', len(out['blocks']))
    if len(out['blocks'])==0:
        return 0
    mid_sec = int(len(out['blocks'])/2)
    if 'lines' in list(out['blocks'][mid_sec].keys()):
        word_length = len(out['blocks'][mid_sec]['lines'])
    else:
        word_length = 0
    mx_len = min(20, word_length)
    for i in range(mx_len):
        dir = out['blocks'][mid_sec]['lines'][i]['dir']
        if dir==(1.0,0.0):
            no_rot+=1
        elif dir==(0.0,1.0):
            left_rot+=1
        elif dir==(0.0,-1.0):
            right_rot+=1
    mx_val = max(no_rot,left_rot,right_rot)
    if mx_val==no_rot:
        return 0
    elif mx_val==left_rot:
        return -90
    else:
        return 90

def determine_rotation(words):
    vertical_up = 0
    vertical_down = 0
    horizontal = 0

    for word in words:
        x0, y0, x1, y1 = word[:4]
        dx = x1 - x0
        dy = y1 - y0

        if abs(dy) > abs(dx):  # Vertical orientation
            if dy > 0:
                vertical_down += 1  # Top to bottom → rotated 90°
            else:
                vertical_up += 1    # Bottom to top → rotated -90°
        else:
            horizontal += 1

    if vertical_down > vertical_up and vertical_down > horizontal:
        return -90  # Rotate counter-clockwise to fix 90° rotation
    elif vertical_up > vertical_down and vertical_up > horizontal:
        return 90   # Rotate clockwise to fix -90° rotation
    else:
        return 0    # No rotation needed

def rotate_pdf_based_on_text_orientation(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    for i, page in enumerate(doc):
        #longest_words = get_longest_words(page)
        
        rotation = get_longest_words(page)
        print(i,'-->', rotation)
        if rotation != 0:
            page.set_rotation((page.rotation + rotation) % 360)
            print(f"Rotated page {i + 1} by {rotation} degrees.")
    doc.save(output_pdf)
    doc.close()
    print(f"Saved rotated PDF as: {output_pdf}")

# Example usage
input_pdf_path = "/home/test/jitender/financial-insights-main/financial-insights-main/Ryanair-2024-Annual-Report.pdf"
output_pdf_path = "SNB_rotated.pdf"
rotate_pdf_based_on_text_orientation(input_pdf_path, output_pdf_path)
