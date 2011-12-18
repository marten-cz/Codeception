<?php

$spec = Pearfarm_PackageSpec::create(array(Pearfarm_PackageSpec::OPT_BASEDIR => dirname(__FILE__)))
             ->setName('Codeception')
             ->setChannel('DavertMik.github.com/pear')
             ->setSummary('Full-stack PHP testing BDD framework.')
             ->setDescription('Codeception is new PHP full-stack testing framework. Inspired by BDD, it provides you absolutely new way for writing acceptance, functional and even unit tests. Powered by PHPUnit 3.6.')
             ->setReleaseVersion('1.0.1')
             ->setReleaseStability('stable')
             ->setApiVersion('1.0.0')
             ->setApiStability('stable')
             ->setLicense(Pearfarm_PackageSpec::LICENSE_MIT)
             ->setNotes('Initial release.')
             ->addMaintainer('lead', 'Michael Bodnarchuk', 'DavertMik', 'davert@mail.ua')
             ->addGitFiles()
             ->addExecutable('codecept')
             ;