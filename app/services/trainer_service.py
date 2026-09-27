from app.utils.exceptions import DuplicateEmailError


class TrainerService:
    def __init__(self, trainer_repository):
        self.trainer_repository = trainer_repository

    class TrainerService:

        def __init__(self, trainer_repository):
            self.trainer_repository = trainer_repository

        def add_trainer(self, trainer):
            return self.trainer_repository.add(trainer)

        def list_trainers(self):
            return self.trainer_repository.get_all()

    def register_trainer(self, trainer):
        existing_member = self.trainer_repository.get_by_email(trainer.email)
        if existing_member:
            raise DuplicateEmailError(trainer.email)
        return self.trainer_repository.add(trainer)


    def deactivate_trainer(self, trainer_id):
        trainer = self.trainer_repository.get_by_id(trainer_id)
        if trainer is None:
            return False
        trainer.is_active = False
        self.trainer_repository.update(trainer)
        return True

    def list_active_trainer(self):
        trainers = self.trainer_repository.get_all()
        trainer_active = []
        for trainer in trainers:
            if trainer.is_active:
                trainer_active.append(trainer)
        return trainer_active

    def add_trainer(self, trainer):
        return self.trainer_repository.add(trainer)

    def list_trainers(self):
            return self.trainer_repository.get_all()