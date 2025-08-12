import pickle, gzip

# Read the original pickle file
with open("similarity.pkl", "rb") as f:
    data = pickle.load(f)

# Save it as a compressed gzip file
with gzip.open("similarity.pkl.gz", "wb") as f:
    pickle.dump(data, f)

print("✅ Compression complete: similarity.pkl.gz created")
