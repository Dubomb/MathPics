import 'package:camera/camera.dart';
import 'package:flutter/material.dart';

class CameraDisplay extends StatefulWidget {
  final CameraController controller;
  final Future<void> initializeControllerFuture;

  const CameraDisplay({super.key, required this.controller, required this.initializeControllerFuture});

  @override
  State<CameraDisplay> createState() => _CameraDisplayState();
}

class _CameraDisplayState extends State<CameraDisplay> {
  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: widget.initializeControllerFuture,
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          return CameraPreview(widget.controller);
        } else {
          return const Column(
            children: [
              Text('Waiting for camera permission.'),
              CircularProgressIndicator(),
            ],
          );
        }
      }
    );
  }
}