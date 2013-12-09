class InformixRouter(object):
    def db_for_read(self, model,**hints):
        if model._meta.app_label=='informix':
            return 'informix'
        return None
        
    def db_for_write(self,model,**hints):
         if model._meta.app_label=='informix':
            return 'informix'
         return None
        
    def allow_syncdb(self,db,model):
        if db == 'informix':
            return model._meta.app_label == 'informix'
        elif model._meta.app_label == 'informix':
            return True
        return None
            