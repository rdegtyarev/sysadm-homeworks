# Домашнее задание к занятию «2.4. Инструменты Git»

Для выполнения заданий в этом разделе давайте склонируем репозиторий с исходным кодом 
терраформа https://github.com/hashicorp/terraform 

В виде результата напишите текстом ответы на вопросы и каким образом эти ответы были получены. 

1. Найдите полный хеш и комментарий коммита, хеш которого начинается на `aefea`.  
```bash
roman@Laptop:~/PycharmProjects/terraform$ git show aefea
commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545
Author: Alisdair McDiarmid <alisdair@users.noreply.github.com>
Date:   Thu Jun 18 10:29:58 2020 -0400

    Update CHANGELOG.md

...
```
2. Какому тегу соответствует коммит `85024d3`?  
```bash
git show --pretty=oneline 85024d3
85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23) v0.12.23
```
 Тег v0.12.23

3. Сколько родителей у коммита `b8d720`? Напишите их хеши.  
```bash
git show b8d720^
commit 56cd7859e05c36c06b56d013b55a252d0bb7e158
Merge: 58dcac4b7 ffbcf5581
Author: Chris Griggs <cgriggs@hashicorp.com>
Date:   Mon Jan 13 13:19:09 2020 -0800

    Merge pull request #23857 from hashicorp/cgriggs01-stable
    
    [cherry-pick]add checkpoint links
```
 Комит имеет двух родителей. Результат merge коммитов 58dcac4b7 ffbcf5581

4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами  v0.12.23 и v0.12.24.  

 Получаем хеши комита, помеченного тегом v0.12.23.
```bash
git show v0.12.23
tag v0.12.23
Tagger: TeamCity <teamcity@ip-192-168-0-113.us-west-2.compute.internal>
Date:   Thu Mar 5 20:56:10 2020 +0000

v0.12.23
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1

iQEcBAABAgAGBQJeYWdqAAoJEFGFLYc0j/xMPDIH/jYhX2jO10Ov8y3zSWPbvKWX
Q8MbyKs7c65+9NRNbhfIoez6mVUz2VF63sza4HXocm60Ckd38a0xb8gI56XbjDMC
tm440iT7xpd/6NlbDDcIcdppAqEOpdFT6eIK1ndYkn61Ks6KSx5i3SCeSk4wwAvg
jPPoqm1ExJSEjSA+gR2HPJuaHDgoXFng2w9i3gzE7IQiFjdS4fJX4GdJj6Ay4HDM
wU4HTPG84vLEiG5rRR5xm0Pqmzt40a53ihRCrXEYrAHT1dgY9LuYcdYySAAvaXq2
jUTrN9ckGoIaxZpCAOVCHiojxCG09ReBgAYQ6YuBbqtR80RV8TBKdCR9S4n9Wls=
=13hk
-----END PGP SIGNATURE-----

commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23)
```
 Получаем хеши комита, помеченного тегом v0.12.24.
```bash
git show v0.12.24
tag v0.12.24
Tagger: TeamCity <teamcity@ip-192-168-0-237.us-west-2.compute.internal>
Date:   Thu Mar 19 15:04:05 2020 +0000

v0.12.24
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1

iQEcBAABAgAGBQJec4nlAAoJEFGFLYc0j/xMSvoIAK0z57IgGyIs8ghpFaksZkRl
XJOrZjP1szlXRMAoMNkef46VUDNjrdPBo+xSHuRxbxFpC2vQwqtwA3Dk8W/KaX5F
AkJXqtWlpyZiWrNMWsXt0AN8CjiaIF5zgrIWvpawGbPU6APOC6FpQiG8WFUobX9p
yRKMOTARAYO1bNgSr8Tgtvv2djRl3PIe6Im9/qyi7S2cFCV9ql8nRLBMPPvZ5xzr
3gehdozVGSJ2C1rI0R3DXAu+q9W6KZsZOhBEsBb/2X/M9chiH6JDbT7bvvgXX34P
gyvcohmWnVwm5Oaurco1hdZFipN+qGMc3EEB3sqoSW0ASTmjocYr44hT3O7/iD0=
=UdsJ
-----END PGP SIGNATURE-----

commit 33ff1c03bb960b332be3af2e333462dde88b279e (tag: v0.12.24)
```
 Получаем информацию о комитах в этом диапазоне
```bash
git log --pretty=format:'%h %an %ad %s' 85024d3100126de36331c6982bfaac02cdab9e76..33ff1c03bb960b332be3af2e333462dde88b279e
33ff1c03b tf-release-bot Thu Mar 19 15:04:05 2020 +0000 v0.12.24
b14b74c49 Chris Griggs Tue Mar 10 08:59:20 2020 -0700 [Website] vmc provider links
3f235065b Alisdair McDiarmid Thu Mar 19 10:39:31 2020 -0400 Update CHANGELOG.md
6ae64e247 Alisdair McDiarmid Thu Mar 19 10:20:10 2020 -0400 registry: Fix panic when server is unreachable
5c619ca1b Nick Fagerlund Wed Mar 18 12:30:20 2020 -0700 website: Remove links to the getting started guide's old location
06275647e Alisdair McDiarmid Wed Mar 18 10:57:06 2020 -0400 Update CHANGELOG.md
d5f9411f5 Alisdair McDiarmid Tue Mar 17 13:21:35 2020 -0400 command: Fix bug when using terraform login on Windows
4b6d06cc5 Pam Selle Tue Mar 10 12:04:50 2020 -0400 Update CHANGELOG.md
dd01a3507 Kristin Laemmert Thu Mar 5 16:32:43 2020 -0500 Update CHANGELOG.md
225466bc3 tf-release-bot Thu Mar 5 21:12:06 2020 +0000 Cleanup after v0.12.23 release
```

5. Найдите коммит в котором была создана функция `func providerSource`, ее определение в коде выглядит 
так `func providerSource(...)` (вместо троеточего перечислены аргументы).  

 Ищем файл с данной функцией
```bash
git grep 'func providerSource'
provider_source.go:func providerSource(configs []*cliconfig.ProviderInstallation, services *disco.Disco) (getproviders.Source, tfdiags.Diagnostics) {
provider_source.go:func providerSourceForCLIConfigLocation(loc cliconfig.ProviderInstallationLocation, services *disco.Disco) (getproviders.Source, tfdiags.Diagnostics) {
```
 Ищем все изменения данной функции в найденном файле
```bash
git log --oneline -L:providerSource:provider_source.go
5af1e6234 main: Honor explicit provider_installation CLI config when present

diff --git a/provider_source.go b/provider_source.go
--- a/provider_source.go
+++ b/provider_source.go
@@ -20,6 +23,15 @@
-func providerSource(services *disco.Disco) getproviders.Source {
-       // We're not yet using the CLI config here because we've not implemented
-       // yet the new configuration constructs to customize provider search
-       // locations. That'll come later. For now, we just always use the
-       // implicit default provider source.
-       return implicitProviderSource(services)
+func providerSource(configs []*cliconfig.ProviderInstallation, services *disco.Disco) (getproviders.Source, tfdiags.Diagnostics) {
+       if len(configs) == 0 {
+               // If there's no explicit installation configuration then we'll build
+               // up an implicit one with direct registry installation along with
+               // some automatically-selected local filesystem mirrors.
+               return implicitProviderSource(services), nil
+       }
+
+       // There should only be zero or one configurations, which is checked by
+       // the validation logic in the cliconfig package. Therefore we'll just
+       // ignore any additional configurations in here.
+       config := configs[0]
+       return explicitProviderSource(config, services)
+}
+
92d6a30bb main: skip direct provider installation for providers available locally

diff --git a/provider_source.go b/provider_source.go
--- a/provider_source.go
+++ b/provider_source.go
@@ -19,5 +20,6 @@
 func providerSource(services *disco.Disco) getproviders.Source {
        // We're not yet using the CLI config here because we've not implemented
        // yet the new configuration constructs to customize provider search
-       // locations. That'll come later.
-       // For now, we have a fixed set of search directories:
+       // locations. That'll come later. For now, we just always use the
+       // implicit default provider source.
+       return implicitProviderSource(services)
8c928e835 main: Consult local directories as potential mirrors of providers

diff --git a/provider_source.go b/provider_source.go
--- /dev/null
+++ b/provider_source.go
@@ -0,0 +19,5 @@
+func providerSource(services *disco.Disco) getproviders.Source {
+       // We're not yet using the CLI config here because we've not implemented
+       // yet the new configuration constructs to customize provider search
+       // locations. That'll come later.
+       // For now, we have a fixed set of search directories:
```
 Найдено три коммита:
 5af1e6234 main: Honor explicit provider_installation CLI config when present
 92d6a30bb main: skip direct provider installation for providers available locally
 8c928e835 main: Consult local directories as potential mirrors of providers

6. Найдите все коммиты в которых была изменена функция `globalPluginDirs`.  
```bash
git log -S'globalPluginDirs' --oneline
35a058fb3 main: configure credentials from the CLI config file
c0b176109 prevent log output during init
8364383c3 Push plugin discovery down into command package
```
7. Кто автор функции `synchronizedWriters`?  
```bash
git log --pretty=format:'%h %an %ad %s' -S'synchronizedWriters' 
bdfea50cc James Bardin Mon Nov 30 18:02:04 2020 -0500 remove unused
fd4f7eb0b James Bardin Wed Oct 21 13:06:23 2020 -0400 remove prefixed io
5ac311e2a Martin Atkins Wed May 3 16:25:41 2017 -0700 main: synchronize writes to VT100-faker on Windows
```
  Автор Martin Atkins, функция создана в коммите 5ac311e2a


 ---

### Как оформить ДЗ?

## Как сдавать задания

Обязательными к выполнению являются задачи без указания звездочки. Их выполнение необходимо для получения зачета и диплома о профессиональной переподготовке.

Задачи со звездочкой (*) являются дополнительными задачами и/или задачами повышенной сложности. Они не являются обязательными к выполнению, но помогут вам глубже понять тему.

Домашнее задание выполните в файле readme.md в github репозитории. В личном кабинете отправьте на проверку ссылку на .md-файл в вашем репозитории.

Также вы можете выполнить задание в [Google Docs](https://docs.google.com/document/u/0/?tgif=d) и отправить в личном кабинете на проверку ссылку на ваш документ.
Название файла Google Docs должно содержать номер лекции и фамилию студента. Пример названия: "1.1. Введение в DevOps — Сусанна Алиева".

Если необходимо прикрепить дополнительные ссылки, просто добавьте их в свой Google Docs.

Перед тем как выслать ссылку, убедитесь, что ее содержимое не является приватным (открыто на комментирование всем, у кого есть ссылка), иначе преподаватель не сможет проверить работу. Чтобы это проверить, откройте ссылку в браузере в режиме инкогнито.

[Как предоставить доступ к файлам и папкам на Google Диске](https://support.google.com/docs/answer/2494822?hl=ru&co=GENIE.Platform%3DDesktop)

[Как запустить chrome в режиме инкогнито ](https://support.google.com/chrome/answer/95464?co=GENIE.Platform%3DDesktop&hl=ru)

[Как запустить  Safari в режиме инкогнито ](https://support.apple.com/ru-ru/guide/safari/ibrw1069/mac)

Любые вопросы по решению задач задавайте в чате Slack.

---
