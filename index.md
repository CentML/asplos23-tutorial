---
layout: home
title: Agenda
nav_order: 1
permalink: /
---

# Predicting and Optimizing Runtime Performance of Deep Learning Models

## Abstract

In this tutorial, we will introduce techniques to easily find the underutilization and performance bottlenecks of GPUs 
for deep-learning (DL) workloads. After that, we will do a brief introduction to CUDA programming as an example of a 
current way of addressing typical performance bottlenecks and underutilization in DL workloads. And we will wrap it up 
by introducing a new DL compiler Hidet (ASPLOS2023 paper), that allows rapid development of performant tensor programs 
in a higher-level language such as Python.

## Scope and Objectives

This tutorial has the following objectives. First, we will demonstrate how to use modern tools to rapidly profile DNN 
workloads that you can adopt in your day-to-day research and/or work. Second, we will cover the basics of the CUDA 
programming model to provide the necessary background for the motivation of the new DL compiler Hidet. Thirdly, we will 
introduce Hidet and demonstrate its expressive power relative to the CUDA. At the end of this tutorial, you will have 
everything you need to get started with Hidet to rapidly develop performant tensor programs.

<div style="clear: both;"></div>

## Agenda

{: .important}
> To get the most out of the tutorial, please preferably have the following ready when you attend this tutorial:
> 1. Bring a laptop computer with [Visual Studio Code](https://code.visualstudio.com/). Install the [Remote-SSH plugin](https://code.visualstudio.com/docs/remote/ssh), which will be used to launch profiling on a remote workstation.
> 2. (Recommended) Have a remote workstation running Linux with a NVIDIA GPU that you can ssh into. You also need to have Python and CUDA installed. 

{% for module in site.modules %}
{{ module }}
{% endfor %}

<div style="clear: both;"></div>

## Organizers

{% assign organizers = site.staffers | where: 'role', 'Organizer' %}
{% for staffer in organizers %}
{{ staffer }}
{% endfor %}

<div style="clear: both;"></div>

## See also

- [Skyline](https://github.com/CentML/skyline): Interactive performance profiling and debugging tool for PyTorch neural networks.
- [Hidet](https://docs.hidet.org): An open-source efficient deep learning framework.

