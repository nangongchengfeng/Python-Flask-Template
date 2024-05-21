# Python-Flask-Template

## 项目概述

 `Python-Flask-Template` 是一个基于 Flask 框架的 Python 项目模板，旨在提供一个规范化的项目结构，帮助开发者快速搭建和开发 Flask 应用。该模板涵盖了常用的目录结构和功能模块，使得代码组织更为清晰和可维护。 

## 技术架构

本项目采用以下技术栈：

> - **Python Flask**: 轻量级的 Web 框架，用于快速开发 Web 应用。
> - **Flasgger**: 用于生成 Swagger 文档，方便 API 的测试和文档化。
> - **Flask_SQLAlchemy**: 集成 SQLAlchemy ORM，简化数据库操作。
> - **Flask_Migrate**: 通过 Alembic 处理数据库迁移。
> - **PyMySQL**: MySQL 数据库连接器，用于与 MySQL 数据库交互。
> - **Flask_Cors**: 处理跨域资源共享（CORS），允许跨域请求。
> - **APScheduler**: 任务调度器，用于在指定时间间隔运行任务。

- **Python Flask**: Flask 是一个轻量级的 WSGI Web 应用框架。它基于 Werkzeug WSGI 工具箱和 Jinja2 模板引擎，并使用 Python 编写。Flask 提供了一个简单而灵活的框架，适合小型项目和原型开发。
- **Flasgger**: Flasgger 是一个 Flask 扩展，用于生成 Swagger 文档。通过使用 Flasgger，你可以自动生成和展示 API 文档，方便测试和维护。
- **Flask_SQLAlchemy**: Flask-SQLAlchemy 是 SQLAlchemy 的 Flask 扩展，提供了与数据库进行交互的简单方法。它通过 ORM（对象关系映射）简化了数据库操作，使得开发者可以使用 Python 类和对象来操作数据库。
- **Flask_Migrate**: Flask-Migrate 是 Flask-SQLAlchemy 的数据库迁移工具。它使用 Alembic 进行数据库版本控制和迁移管理，允许开发者轻松地进行数据库模式的变更。
- **PyMySQL**: PyMySQL 是一个纯 Python 实现的 MySQL 数据库连接器。它提供了与 MySQL 数据库进行通信的接口，支持大多数 MySQL 数据库的功能。
- **Flask_Cors**: Flask-CORS 是一个 Flask 扩展，用于处理跨域资源共享（CORS）。它允许服务器接收来自不同域的请求，从而支持跨域 HTTP 请求。
- **APScheduler**: APScheduler 是一个 Python 库，用于调度任务。它可以在指定的时间或间隔运行任务，支持多种调度方式，如固定时间间隔、日期调度、间隔调度等。

## 项目结构

```python
Python-Flask-Template/
├─app
│  ├─api
│  │  ├─controller    # 控制器层，用于处理HTTP请求并返回响应
│  │  ├─dao           # 处理数据库的具体操作。调用 Models 层代码与数据库进行交互。
│  │  ├─models        # 模型层，用于定义数据库模型和实体
│  │  ├─service       # 服务层，包含业务逻辑处理
│  ├─common
│  │  ├─result        # 结果处理模块，用于统一处理和返回接口响应
│  │  └─util          # 工具模块，包含一些通用的工具函数和类
│  ├─middleware       # 中间件，包含一些请求处理的中间件
└─logs                # 日志目录，用于存放日志文件
```

### 详细说明

- `app/`: 项目的主应用目录，包含所有的代码模块和业务逻辑。
  - `api/`: API 目录，包含处理 API 请求的相关模块。
    - `controller/`: 控制器层，用于接收和处理 HTTP 请求，调用服务层处理业务逻辑，并返回响应结果。
    - `dao/`: 数据传输对象，用于定义请求和响应的数据结构，确保数据的一致性和完整性。
    - `models/`: 模型层，用于定义数据库模型和实体，通常使用 ORM 框架（如 SQLAlchemy）来与数据库进行交互。
    - `service/`: 服务层，包含具体的业务逻辑处理，将复杂的业务逻辑从控制器中分离出来，使得代码更为简洁和易维护。
  - `common/`: 公共模块，包含项目中通用的工具和辅助函数。
    - `result/`: 结果处理模块，定义统一的响应格式和错误处理机制，确保 API 响应的一致性。
    - `util/`: 工具模块，包含一些常用的工具函数和类，如日期处理、字符串处理等。
  - `middleware/`: 中间件模块，包含一些请求处理的中间件，如身份验证、日志记录等，可以在请求进入控制器之前进行处理。
- `logs/`: 日志目录，用于存放项目运行过程中生成的日志文件，方便调试和错误追踪。

## MVC架构

![1716262741393](images/1716262741393.png)

![1716262886984](images/1716262886984.png)

**详细描述**

- **User**:
  - 用户通过前端发起 HTTP 请求。

- **Controller 控制层**:
  - 接收来自前端的 HTTP 请求
  - 调用 Service 层代码进行业务处理
  - 返回处理结果给前端
- **Service 业务层**:
  - 包含具体的业务逻辑处理
  - 调用 DAO 层代码进行数据访问
  - 返回业务处理结果给 Controller 层
- **DAO 层 (Data Access Object)**:
  - 处理数据库的具体操作
  - 调用 Models 层代码与数据库进行交互
  - 返回数据库操作结果给 Service 层
- **Models 模型层**:
  - 定义数据库的 ORM 模型
  - 提供与数据库表的映射和操作

## 使用说明

 克隆项目代码： 

```
 git clone  https://github.com/nangongchengfeng/Python-Flask-Template.git
```

 安装依赖： 

```
cd Python-Flask-Template
pip install -r requirements.txt
```

或者

```
python deal_package.py  
```

运行项目

```
python  manage.py
```

## 项目演示

http://127.0.0.1:5000/apidocs/#/



![1716261495036](images/1716261495036.png)

![1716261510637](images/1716261510637.png)