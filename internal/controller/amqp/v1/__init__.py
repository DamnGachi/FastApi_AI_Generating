from internal.controller.amqp.v1 import applications
from pkg.rabbitmq.rpc import RPCRouter

router = RPCRouter()
router.include_router(
    applications.router,
    prefix="/applications",
)
