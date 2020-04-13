def __after_init_updatehub_ti():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                        'meta-arm/meta-arm',
                        'meta-ti',
                        'meta-updatehub-ti',
                    ]])

run_after_init(__after_init_updatehub_ti)
