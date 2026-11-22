import matplotlib.pyplot as plt
from collections import Counter

from ps3 import * 

# ---------- Bin prep ----------
def prep_bins_counts():
    raw = [
        "  Water  Bottle ", "can", "Flyers", "banana peel", " ", "BOX", "takeout", "mail", "aluminum",
        "Cup", "GLASS", "glass", "Paper", "water bottle",
        "  box  ", "can", "Aluminum", "Flyers", "mail", "takeout  ", "  cup", "Paper", "glass",
        "water    bottle", "CAN", "box", "Flyers", "banana peel", "paper", "  mail ", "Cup", "glass",
        "takeout", "cup", "mail", "BOX", "flyers", "aluminum", "can", "paper", "glass", "glass",
        "plastic bag", "food waste", "styrofoam", " ", "electronics"
    ]
    before_counts = Counter([s.strip().lower() for s in raw if s.strip()])
    items = raw[:]
    normalize(items)
    swap_equivalents(items, EQUIV)
    remove_contaminants(items, ALLOWED)
    after_counts = Counter(items)
    return before_counts, after_counts


# ---------- Route prep ----------
def prep_routes_three_stages():
    start = [
        ["Ash","Birch"], ["Cedar"], ["Dover","Elm","Fir"], ["Grove"],
        ["Hill","Iris","Juniper","Knoll"], ["Maple"],
        ["Oak","Pine","Quince","Rose","Spruce"], ["Teak","Ulmus"], ["Vine"], ["Willow","Xenia","Yew","Zinnia"]
    ]
    before = [len(r) for r in start]

    stitched = [r[:] for r in start]
    stitch_short_routes(stitched, min_len=3)
    after_stitch = [len(r) for r in stitched]

    balanced = [r[:] for r in start]
    stitch_short_routes(balanced, min_len=3)
    balance_load(balanced)
    after_balance = [len(r) for r in balanced]

    return before, after_stitch, after_balance


# ---------- Queue prep ----------
def prep_queue_curves():
    arrivals = (
        ["plastic","food","cardboard","food","glass","plastic","food","paper","food","glass"] * 4
    )
    q = []
    enqueue_all(q, arrivals)
    before = q[:]
    prioritize(q, lambda x: x == "food")
    after = q[:]
    return before, after


def cumulative_food_fraction(seq):
    x = list(range(1, len(seq)+1))
    y = []
    running_food = 0
    for i, item in enumerate(seq, start=1):
        if item == "food":
            running_food += 1
        y.append(running_food / i)
    return x, y


# ---------- Plotting ----------
def main():
    b_before, b_after = prep_bins_counts()
    r_before, r_after_stitch, r_after_balance = prep_routes_three_stages()
    q_before_seq, q_after_seq = prep_queue_curves()

    # Harmonize labels for bins
    bin_labels = sorted(set(b_before.keys()) | set(b_after.keys()))
    bin_before_vals = [b_before.get(k, 0) for k in bin_labels]
    bin_after_vals = [b_after.get(k, 0) for k in bin_labels]

    # --- Plot ---
    fig = plt.figure(figsize=(12, 10))

    # 1) Bins
    ax1 = fig.add_subplot(3, 1, 1)
    x = range(len(bin_labels))
    width = 0.4
    ax1.bar([i - width/2 for i in x], bin_before_vals, width, label="Before")
    ax1.bar([i + width/2 for i in x], bin_after_vals, width, label="After")
    ax1.set_xticks(list(x))
    ax1.set_xticklabels(bin_labels, rotation=20)
    ax1.set_title("Bin Categories: Before vs After Cleaning/Filtering")
    ax1.set_ylabel("Count")
    ax1.legend()

    # 2) Routes (3 stages)
    ax2 = fig.add_subplot(3, 1, 2)
    rmax = max(len(r_before), len(r_after_stitch), len(r_after_balance))
    route_labels = [f"R{i}" for i in range(rmax)]
    # pad with zeros for alignment
    rb = r_before + [0]*(rmax - len(r_before))
    rs = r_after_stitch + [0]*(rmax - len(r_after_stitch))
    ra = r_after_balance + [0]*(rmax - len(r_after_balance))
    width = 0.25
    x = range(rmax)
    ax2.bar([i - width for i in x], rb, width, label="Before")
    ax2.bar(x, rs, width, label="After Stitch")
    ax2.bar([i + width for i in x], ra, width, label="After Balance")
    ax2.set_xticks(list(x))
    ax2.set_xticklabels(route_labels, rotation=20)
    ax2.set_title("Route Lengths: Three Stages")
    ax2.set_ylabel("Stops per Route")
    ax2.legend()

    # 3) Queue (fraction curve)
    ax3 = fig.add_subplot(3, 1, 3)
    x_before, y_before = cumulative_food_fraction(q_before_seq)
    x_after, y_after = cumulative_food_fraction(q_after_seq)
    ax3.plot(x_before, y_before, label="Before")
    ax3.plot(x_after, y_after, label="After Prioritization")
    ax3.set_title("Queue Prioritization: Food Nearer to Front")
    ax3.set_xlabel("Front-of-line length k")
    ax3.set_ylabel("Fraction food in first k")
    ax3.set_ylim(0, 1)
    ax3.legend()

    fig.tight_layout()
    return plt.show()

main()
