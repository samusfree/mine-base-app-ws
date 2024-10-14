from dependency_injector import containers, providers

from api.controller.user_controller import UserController
from api.repository.user_repository import UserRepository
from api.service.user_service import UserService


class APPConfig(containers.DeclarativeContainer):
    config = providers.Configuration()


class APPRepositories(containers.DeclarativeContainer):
    user_repository = providers.Factory(UserRepository)


class APPServices(containers.DeclarativeContainer):
    user_service = providers.Factory(
        UserService, user_repository=APPRepositories.user_repository
    )


class AppControllers(containers.DeclarativeContainer):
    user_controller = providers.Factory(
        UserController, user_service=APPServices.user_service
    )


class APPContainer(containers.DeclarativeContainer):
    config: APPConfig = providers.Container(APPConfig)
    repositories: APPRepositories = providers.Container(APPRepositories)
    services: APPServices = providers.Container(APPServices)
    controllers: AppControllers = providers.Container(AppControllers)
