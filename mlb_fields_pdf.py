import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from mlb_field_dimensions import TEAM_FIELD_FUNCTIONS, draw_single_field, fetch_team_logo

# --- PDF Save Directory ---
script_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(script_dir, "mlb_fields_pdf")
os.makedirs(save_dir, exist_ok=True)
output_path = os.path.join(save_dir, "mlb_all_field_layouts_grid.pdf")

# --- Main PDF Function ---
def create_field_grid_pdf():
    team_list = list(TEAM_FIELD_FUNCTIONS.items())
    cols = 5
    rows = 6
    fig, axs = plt.subplots(rows, cols, figsize=(10, 12))
    fig.suptitle("MLB Outfield Layouts", fontsize=24, fontweight='bold')

    for idx, (team_name, field_func) in enumerate(team_list):
        r = idx // cols
        c = idx % cols
        logo_image = fetch_team_logo(team_name)
        if field_func:
            draw_single_field(axs[r, c], team_name, field_func, logo_image=logo_image)
            axs[r, c].set_title(team_name, fontsize=10)
        else:
            print(f"No field function for {team_name}")
            axs[r, c].set_title(f"{team_name} - No Data", fontsize=10)
            axs[r, c].axis("off")

    plt.tight_layout(rect=[0, 0, 1, 0.98])
    with PdfPages(output_path) as pdf:
        pdf.savefig(fig)
    plt.close()
    print(f"✅ PDF created at: {output_path}")

# --- Run ---
if __name__ == "__main__":
    create_field_grid_pdf()
