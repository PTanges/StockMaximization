import SPMP_ExhaustiveApproach
import SPMP_DynamicApproach
import SPMP_SETTINGS


def main():
    SPMP_ExhaustiveApproach.exhaustive_method(SPMP_SETTINGS.inputFileName, SPMP_SETTINGS.outputFileNameEP)
    SPMP_DynamicApproach.dynamic_method(SPMP_SETTINGS.inputFileName, SPMP_SETTINGS.outputFileNameDP)


if __name__ == "__main__":
    main()
