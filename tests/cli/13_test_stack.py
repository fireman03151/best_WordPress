from wo.utils import test
from wo.cli.main import get_test_app


class CliTestCaseStack(test.WOTestCase):

    def test_wo_cli(self):
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install(self):
        argv = ['stack', 'install']
        with self.make_app(argv=argv) as app:
            app.run()
            self.eq(app.pargs.stack.install)


    def test_wo_cli_stack_install_web(self):
        self.app = get_test_app(argv=['stack', 'install', '--web'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_admin(self):
        self.app = get_test_app(argv=['stack', 'install', '--admin'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_nginx(self):
        self.app = get_test_app(argv=['stack', 'install', '--nginx'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_php(self):
        self.app = get_test_app(argv=['stack', 'install', '--php'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_mysql(self):
        self.app = get_test_app(argv=['stack', 'install', '--mysql'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_wpcli(self):
        self.app = get_test_app(argv=['stack', 'install', '--wpcli'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_phpmyadmin(self):
        self.app = get_test_app(argv=['stack', 'install', '--phpmyadmin'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_adminer(self):
        self.app = get_test_app(argv=['stack', 'install', '--adminer'])
        self.app.setup()
        self.app.run()
        self.app.close()

    def test_wo_cli_stack_install_utils(self):
        self.app = get_test_app(argv=['stack', 'install', '--utils'])
        self.app.setup()
        self.app.run()
        self.app.close()
