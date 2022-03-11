from lib import IntelligencePlacerImpl as Impl


def find_objects(path_to_image, print_errors=True):
    impl = Impl.IntelligencePlacerImpl()
    result = impl.find_objects(path_to_image)
    if result is None and print_errors:
        print(impl.get_last_err_message())
    return result
