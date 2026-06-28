jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install dependencies
        run: |
          sudo apt update
          sudo apt install -y python3-pip git zip unzip openjdk-17-jdk
          pip install buildozer cython

      - name: Accept Android licenses
        run: yes | sdkmanager --licenses || true

      - name: Build APK
        run: buildozer android debug
