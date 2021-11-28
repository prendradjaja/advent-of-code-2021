import sys


# Remove .releaselevel and .serial parts of version_info so that == >= etc
# work properly against it
_version = sys.version_info[:3]


_requirements_by_feature = {
    'ordered-dicts': (3, 7, 0),
    'functools-cache': (3, 9, 0),
}


def require(*features):
    missing_features = [
        feat
        for feat in features
        if _requirements_by_feature[feat] > _version
    ]
    min_supported = max(
        (_requirements_by_feature[feat] for feat in features),
        default=(0, 0, 0)
    )
    min_supported_str = '.'.join(str(part) for part in min_supported)

    if missing_features:
        raise Exception(f'Unsupported Python version. Required version: {min_supported_str}. Missing features: {", ".join(missing_features)}')
