from comics.settings.testing import *

# Test runner with code coverage
TEST_RUNNER = 'comics.utils.test_runner.test_runner_with_coverage'
COVERAGE_MODULES = (
    'comics.core.context_processors',
    'comics.core.feeds',
    'comics.core.managers',
    'comics.core.models',
    'comics.core.templatetags.versioned_media',
    'comics.core.utils.comic_releases',
    'comics.core.utils.navigation',
    'comics.core.utils.time_frames',
    'comics.core.views',
    'comics.crawler.base',
    'comics.crawler.management.commands.crawlcomics',
    'comics.crawler.management.commands.loadcomicmeta',
    'comics.crawler.meta',
    'comics.crawler.runner',
    'comics.crawler.utils',
    'comics.crawler.utils.webparser',
    'comics.feedback.forms',
    'comics.feedback.views',
    'comics.sets.feeds',
    'comics.sets.forms',
    'comics.sets.middleware',
    'comics.sets.models',
    'comics.sets.views',
    'comics.utils.commands',
    'comics.utils.disk_import',
    'comics.utils.hash',
    'comics.utils.management.commands.importcomics',
)