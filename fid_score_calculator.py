import argparse
from PIL import Image
from cleanfid.fid import compute_fid
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def main():
    parser = argparse.ArgumentParser(description="Compute FID score between two images.")
    parser.add_argument("image1", type=str, help="Path to the first image")
    parser.add_argument("image2", type=str, help="Path to the second image")
    args = parser.parse_args()

    print(args.image1)
    print(args.image2)
    
    # Compute FID score
    fid_score = compute_fid(args.image1, args.image2)

    print(f"FID score between {args.image1} and {args.image2}: {fid_score}")

if __name__ == "__main__":
    main()
