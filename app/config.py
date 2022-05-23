class DevConfig:
  DEBUG = False


class TestConfig:
  DEBUG = True


configurations = {
  "dev": DevConfig,
  "test": TestConfig,
}