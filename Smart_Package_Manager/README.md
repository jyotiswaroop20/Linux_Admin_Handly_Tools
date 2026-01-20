# SmartPkg – Smart Package Manager

SmartPkg is an advanced **Linux package management automation tool** designed for system administrators. It installs packages, manages services, handles dependencies, provides rollback on failure, and works across **Debian and Fedora family distributions** — all using a **single native-style command**.

This tool is built to reduce manual effort, avoid mistakes, and give **clear, Ansible-like output** while remaining simple and powerful.

---

## 🚀 Key Features

✅ **Cross-distro support**
Automatically detects the OS and works on:

* Debian / Ubuntu (APT based)
* RHEL / CentOS / Rocky / Alma / Fedora (DNF based)

✅ **Single & multiple package install**
Install one or many packages in a single command.

✅ **Dependency auto-resolve**
All required dependencies are resolved automatically by the package manager.

✅ **Pre-install verification**
Checks if a package is already installed before taking action.

✅ **Service auto-detection**
Automatically detects whether an installed package provides a systemd service.

✅ **Service management (if applicable)**

* Starts the service
* Enables it at boot time
* Verifies service status (up & running)

✅ **Non-service package verification**
If the package is not a service, SmartPkg verifies installation using native package queries.

✅ **Dry-run mode (safe simulation)**
Simulates the complete process without making any system changes.

✅ **Rollback on failure**
If installation fails midway, all newly installed packages are automatically removed.

✅ **Centralized logging**
All operations are logged to:

```
/var/log/smartpkg.log
```

✅ **Ansible-like output**
Clear and readable output:

* `ok`
* `changed`
* `failed`

✅ **Root & sudo compatible**
Can be executed by `root` or normal users with `sudo` access.

✅ **Native Linux command style**
Feels like a real Linux command, not a script.

✅ **Packaging ready**
Designed to be easily packaged as:

* `.rpm`
* `.deb`

---

## 📦 Installation (Make It a System Command)

Follow these steps to use SmartPkg like a native Linux command.

### Step 1: Make the script executable

```bash
chmod +x smartpkg
```

### Step 2: Copy it to system PATH

```bash
sudo cp smartpkg /usr/local/bin/
```

### Step 3: Verify installation

```bash
which smartpkg
```

Expected output:

```text
/usr/local/bin/smartpkg
```

Now SmartPkg can be executed from **any directory**.

---

## 🧪 Usage Examples

### Dry-run (simulation only)

```bash
smartpkg --dry-run nginx httpd git vim gcc
```
START smartpkg | OS=fedora | dry_run=True

would-change: package[nginx] would be installed
would-change: service[nginx] would be enabled and started

would-change: package[httpd] would be installed
would-change: service[httpd] would be enabled and started

ok: package[git] already installed
ok: package[vim] already installed
ok: package[gcc] already installed

END smartpkg | DRY-RUN SUCCESS


### Normal installation

```bash
sudo smartpkg nginx
```

### Multiple packages at once

```bash
sudo smartpkg nginx httpd
```

---

## 📤 Output Style (Example)

```text
START smartpkg | OS=fedora | dry_run=True
DRY-RUN | dnf install -y nginx httpd
changed: package[nginx] installed
ok: package[nginx] started and enabled
changed: package[httpd] installed
ok: service[httpd] started and enabled
ok: service[httpd] is running
END smartpkg | SUCCESS
```

---

## 🔐 Permissions & Security

* Requires root privileges
* Works with:

  ```bash
  sudo smartpkg <packages>
  ```
* Uses native system package managers (APT / DNF)
* No hardcoded credentials

---

## 📁 Logging

All actions, errors, and rollbacks are logged for auditing and troubleshooting:

```text
/var/log/smartpkg.log
```

---

## 🎯 Why SmartPkg?

Normally, a system administrator has to:

1. Install packages
2. Resolve dependencies
3. Check if a service exists
4. Start the service
5. Enable it at boot
6. Verify status
7. Handle failures manually

**SmartPkg does all of this in one command.**

---

## 🛠️ Designed For

* Linux System Administrators
* DevOps Engineers
* Production & Enterprise servers
* Automation-focused environments

---

## 👤 Author

**Jyotiswaroop Tripathi**
Linux System Administrator

---

✅ SmartPkg is built to be **simple, safe, powerful, and production-ready**.
