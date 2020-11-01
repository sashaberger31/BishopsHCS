class PrimaryRouter:
    def db_for_read(self, model, **hints):
        try:
            if model.dev_type == 'use_backend':
                return 'read_only'
            else:
                return 'default'
        except AttributeError:
            return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app, model_name=None, **hints):
        if db == 'read_only':
            return False
        else:
            return True
