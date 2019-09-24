from wo.utils import test
from wo.cli.main import get_test_app


class CliTestCaseStack(test.WOTestCase):

    def test_wo_cli(self):
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_services_status_nginx(self):
        self.app = get_test_app(argv=['stack', 'status', '--nginx'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_services_status_php_fpm(self):
        self.app = get_test_app(argv=['stack', 'status', '--php'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_services_status_mysql(self):
        self.app = get_test_app(argv=['stack', 'status', '--mysql'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_services_status_all(self):
        self.app = get_test_app(argv=['stack', 'status'])
        self.app.setup()
        self.app.run()
        self.app.close()
