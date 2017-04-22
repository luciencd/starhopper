import skyinterface

if __name__ == "__main__":
    lucien = skyinterface.User(latitude=42.7284,longitude=73.6918)

    print lucien.clear_dark_sky.getCloudCover()
