from classes.sphere import Sphere


def main():

    radius = float(input("Inserisci il raggio della sfera (in metri): "))


    sphere = Sphere(radius)


    print(f"Volume della sfera: {sphere.volume()} metri cubi")
    print(f"Superficie della sfera: {sphere.surface_area()} metri quadrati")

if __name__ == "__main__":
    main()