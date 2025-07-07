import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot_chain(ledger):
    fig, ax = plt.subplots(figsize=(2 * len(ledger.chain), 3))
    y = 0.5
    for i, block in enumerate(ledger.chain):
        x = i * 2
        # Draw block as rectangle
        rect = Rectangle((x, y), 1.5, 1, linewidth=1, edgecolor='black', facecolor='lightblue')
        ax.add_patch(rect)
        # Block label: index, hash (truncated), tx count, creator
        creator = getattr(block.signer_public_key, 'agent_name', 'Genesis' if block.index == 0 else 'Agent')
        ax.text(x + 0.75, y + 0.8, f"Block {block.index}", ha='center', fontsize=10, weight='bold')
        ax.text(x + 0.75, y + 0.6, f"Txs: {len(block.transactions)}", ha='center', fontsize=9)
        ax.text(x + 0.75, y + 0.4, f"Hash: {block.hash[:8]}...", ha='center', fontsize=8)
        if block.index == 0:
            ax.text(x + 0.75, y + 0.2, f"Creator: Genesis", ha='center', fontsize=8, color='gray')
        else:
            ax.text(x + 0.75, y + 0.2, f"Creator: Agent", ha='center', fontsize=8, color='gray')
        # Draw arrow to next block
        if i < len(ledger.chain) - 1:
            ax.annotate('', xy=(x + 1.5, y + 0.5), xytext=(x + 2, y + 0.5),
                        arrowprops=dict(facecolor='gray', shrink=0.05, width=2, headwidth=8))
    ax.set_xlim(-0.5, len(ledger.chain) * 2)
    ax.set_ylim(0, 2)
    ax.axis('off')
    plt.title('Blockchain: Each Block Shows Index, Transactions, Hash, Creator')
    plt.tight_layout()
    plt.show() 