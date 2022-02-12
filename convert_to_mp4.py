import argparse
import sys
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(True):
    ret, frame = cap.read()
    out.write(frame)
    # print("Frame")
    # print(frame)
    cv2.imshow('frame', frame)
    c = cv2.waitKey(1)
    if c & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


def convert_to_mp4(args):
    try:
        cap = cv2.VideoCapture(args.source)
        cap.set(3, 640)  # width
        cap.set(4, 480)  # height

        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        out    = cv2.VideoWriter(f"{args.destination}/output.mp4", fourcc, 30.0, (640, 480))

        while True:
            ret, frame = cap.read()
            out.write(frame)
            c = cv2.imshow("frame", frame)
            if c & 0xFF == ord("q"):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

        return "Video is converted to mp4 format"
    except Exception as e:
        return "Something happened. Try again"


def calc(args):
    if args.o == "add":
        return args.x + args.y
    elif args.o == "mul":
        return args.x * args.y
    elif args.o == "sub":
        return args.x - args.y
    elif args.o == "div":
        return args.x / args.y
    else:
        return "Something went wrong"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=float, default=1.0, help="Enter first number for calculation")
    parser.add_argument("--y", type=float, default=3.0, help="Enter second number for calculation")
    parser.add_argument("--o", type=str, default="add", help="Enter the operation type")

    parser.add_argument("--source", type=str, help="Give the path where the .mp4v file is located")
    parser.add_argument("--destination", type=str, help="Where the converted .mp4 file will store (path of the directory)")

    args = parser.parse_args()
    sys.stdout.write()

    
    args = parser.parse_args(convert_to_mp4(args))
    # print(args)
    # sys.stdout.write(str(calc(args)))

# C:\Users\sayan\OneDrive\Documents\Chemical Engineering\CRE Lab