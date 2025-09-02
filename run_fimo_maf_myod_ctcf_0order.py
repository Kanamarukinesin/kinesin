import os
import subprocess

motif_file = "MAF_MYOD_CTCF.meme"
bgfile = "bg.all_species.0order"
out_base = "fimo_maf_myod_ctcf_0order_myh3-gas7"
fasta_dir = "../myh3-gas7"

# 各種生物種
species_list = [
    "baboon", "bushbaby", "chimpanzee", "gorilla", "greenmonkey",
    "human", "marmoset", "mouse", "mouselemur", "orangutan", "rhesus", "slowloris"
]

for sp in species_list:
    fasta = os.path.join(fasta_dir, f"myh3-gas7_{sp}.fa")
    out_dir = os.path.join(out_base, f"fimo_out_{sp}")
    os.makedirs(out_dir, exist_ok=True)

    print(f"[FIMO] Running for {sp} …")

    cmd = [
        "fimo",
        "--bgfile", bgfile,
        "--thresh", "1e-4",  # 必要に応じて 1e-3 や 1e-2 に緩和
        "--verbosity", "1",
        "--oc", out_dir,
        motif_file,
        fasta
    ]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {sp} で FIMO 実行に失敗しました: {e}")
        continue

print("[DONE] すべての種に対して0-order FIMO完了。")
